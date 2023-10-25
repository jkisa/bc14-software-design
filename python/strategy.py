# Strategy interface
class AuthenticationStrategy:
    def login(self, username, password):
        pass

    def logout(self):
        pass

# Concrete Strategies
class BasicAuthStrategy(AuthenticationStrategy):
    def login(self, username, password):
        if username == 'senjack' and password == 'password':
            return "Logged in with Basic Auth."

    def logout(self):
        return "Logged out from Basic Auth."

class AdvancedAuthStrategy(AuthenticationStrategy):
    def login(self, username, password):
        if username == 'demetira' and password == 'demetira1':
            return "Logged in with Advanced Auth."

    def logout(self):
        return "Logged out from Advanced Auth."

# Example usage
basic_auth = BasicAuthStrategy()
advanced_auth = AdvancedAuthStrategy()

# Implement an IAMLogger to use the strategies
class IAMLogger:
    def __init__(self, auth_strategy):
        self.auth_strategy = auth_strategy

    def login(self, username, password):
        return self.auth_strategy.login(username, password)

    def logout(self):
        return self.auth_strategy.logout()

logger = IAMLogger(basic_auth)
result1 = logger.login('senjack', 'password')
logout_result1 = logger.logout()

logger = IAMLogger(advanced_auth)
result2 = logger.login('demetira', 'demetira1')
logout_result2 = logger.logout()

print(result1)       # Output: "Logged in with Basic Auth."
print(logout_result1) # Output: "Logged out from Basic Auth."
print(result2)       # Output: "Logged in with Advanced Auth."
print(logout_result2) # Output: "Logged out from Advanced Auth."

