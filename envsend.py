import os
# from dotenv import load_dotenv

# project_folder = os.path.expanduser('~/proto/basic_sayhello_pythondocker')
# load_dotenv(os.path.join("project_folder", '.env'))


user = os.getenv("USER")
print(user)

    