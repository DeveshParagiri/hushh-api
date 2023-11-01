def auth_check(token):
    if not token:
        return {"status": 0, "message": f"Auth Token Missing"}

    if token:
        parts = token.split()
        if len(parts) == 2 and parts[0].lower() == "bearer":
            token = parts[1]
            # You now have the Bearer token, and you can perform any necessary authentication or authorization checks.
            if token == "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9":
                return {"status": 1, "response": f"Bearer token: {token}"}
            else:
                return {"status": 0, "response": f"Invalid Token"}
        else:
            return {"status": 2, "response": f"Invalid Authorization header format"}
    else:
        return {"status": 2, "response": f"Token Missing"}
