def chai_serve(flavour):
    try:
        print(f"preparing {flavour} chai...")
        if flavour == "unknown":
            raise ValueError("we dont know that flavour")
    except ValueError as e:
        print("Error: ", e)
    else:
        print(f"here is your {flavour} chai")
    finally:
        print("next customer please")
        
chai_serve("ginger")
chai_serve("unknown")