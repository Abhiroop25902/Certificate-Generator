# Ceritificate Generator

Will generate a list of Participation Certificate and also send emails to them

## Steps (WIP)

1. make `./login_credential.txt` in following format
    ```
    email password
    ```
    - I know the security reason for this and for that I have added this file in gitignore so that this file doesn't go to the internet.

2. update `contact_list.txt` with the following format
    ```
    person1_name person1_email
    person2_name person2_email
    ...
    ```

3. edit `MAIL_SUBJECT` to setup subject line for email

3. update `./message.txt` to setup the message format according to [Template String](https://docs.python.org/3.5/library/string.html#template-strings)

4. run `main.py`

## Note for sending mail via gmail

gmail blocks this scripted mail send behavior, to allow this go to Google Account Setting -> Security -> Less Secure App Access -> Turn On

## Future Addition possible

-   Do something about plaintext login credential
-   turn contact_list.txt to .csv and use pandas to hopefully simplify thing
