
# # - Import password reset token generator

# from django.contrib.auth.tokens import PasswordResetTokenGenerator
# from django.utils import six


# # - Password reset token generator method

# class UserVerificationTokenGenerator(PasswordResetTokenGenerator):
#     def _make_hash_value(self, user, timestamp):
#         user_id = six.text_type(user.pk)
#         ts = six.text_type(timestamp)
#         is_active = six.text_type(user.is_active)
#         return f"{user_id}{ts}{is_active}"

# user_tokenizer_generate = UserVerificationTokenGenerator()

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