# Import password reset token generator
from django.contrib.auth.tokens import PasswordResetTokenGenerator

# Password reset token generator method
class UserVerificationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        user_id = str(user.pk)
        ts = str(timestamp)
        is_active = str(user.is_active)
        return f"{user_id}{ts}{is_active}"

# Create an instance of the token generator
user_tokenizer_generate = UserVerificationTokenGenerator()
