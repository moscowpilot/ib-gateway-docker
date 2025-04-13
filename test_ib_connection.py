from ib_insync import *
import time
import sys

def test_ib_connection():
    # Create IB instance
    ib = IB()
    
    try:
        # Connect to IB Gateway
        # Port 4001 is for live trading, 4002 for paper trading
        ib.connect('127.0.0.1', 4001, clientId=1)
        
        # Wait for connection
        time.sleep(2)
        
        # Check if we're connected
        if ib.isConnected():
            print("✅ Successfully connected to IB Gateway!")
            
            # Get server time to verify connection is working
            server_time = ib.reqCurrentTime()
            print(f"Server time: {server_time}")
            
            # Get account summary
            accounts = ib.managedAccounts()
            print(f"Connected accounts: {accounts}")
            
            return True
        else:
            print("❌ Failed to connect to IB Gateway")
            return False
            
    except Exception as e:
        print(f"❌ Error connecting to IB Gateway: {str(e)}")
        return False
    finally:
        # Disconnect
        ib.disconnect()

if __name__ == "__main__":
    print("Testing IB Gateway connection...")
    success = test_ib_connection()
    sys.exit(0 if success else 1) 