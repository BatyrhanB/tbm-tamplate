from pymongo.errors import WriteError

from src.settings.mongo_db import codes_collection


async def add_otp_code(otp_data: dict) -> dict:
    try:
        email_address = otp_data.get("email")

        if not email_address:
            raise ValueError("Email address is missing in otp_data")

        result = await codes_collection.update_one(
            {"email": email_address}, {"$set": otp_data}, upsert=True
        )

        if result.upserted_id:
            return {"_id": result.upserted_id}
        else:
            return {"message": "OTP updated successfully"}

    except WriteError as e:
        print(f"Error while inserting/updating OTP data: {e}")
        return None
    except ValueError as ve:
        print(f"Value error: {ve}")
        return None
