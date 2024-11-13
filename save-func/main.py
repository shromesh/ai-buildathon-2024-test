import functions_framework
from google.cloud import firestore
from datetime import datetime

# Firestoreクライアントを初期化
db = firestore.Client()


@functions_framework.http
def save_data_http(request):
    """HTTP Cloud Function to save data with a timestamp and user name in Firestore.

    Args:
        request (flask.Request): The request object containing JSON data.
    Returns:
        A response indicating success or error message.
    """
    # JSONリクエストデータを取得
    request_json = request.get_json(silent=True)

    # 必要なフィールドが存在するかを確認
    if request_json and "data" in request_json and "user_name" in request_json:
        try:
            # タイムスタンプ、user_name付きデータを構築
            data_with_timestamp = {
                "datetime": datetime.now(),
                "user_name": request_json["user_name"],
                "data": request_json["data"],
            }

            # Firestoreのdefaultデータベースのdata_collectionにデータを追加
            doc_ref = db.collection("data_collection").add(data_with_timestamp)
            doc_id = doc_ref[1].id  # 追加されたドキュメントID

            return f"Data saved successfully with document ID: {doc_id}", 200

        except Exception as e:
            return f"An error occurred: {str(e)}", 500
    else:
        return (
            "Invalid request: 'data' and 'user_name' fields are required in JSON.",
            400,
        )
