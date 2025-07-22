# mcp.py
import uuid

def create_mcp(sender, receiver, msg_type, payload):
    return {
        "type": msg_type,
        "sender": sender,
        "receiver": receiver,
        "trace_id": str(uuid.uuid4()),
        "payload": payload
    }
