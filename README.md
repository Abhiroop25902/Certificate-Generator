# Ceritificate Generator

Will generate a list of Participation Certificate and also send emails to them

## Steps (WIP)
1.  ```bash
    pip3 install -r requirements.txt
    ```

1. make `./.env` in following format
    ```
    EMAIL = <your_email>
    PASSWORD = <your_password>
    ```

2. update `contact_list.csv` with the following format
    ```csv
    person1_name,person1_email
    person2_name,person2_email
    ...
    ```

3. edit `MAIL_SUBJECT`, `CC`, and `BCC` 

3. update `./message.txt` to setup the message format according to [Template String](https://docs.python.org/3.5/library/string.html#template-strings)

4. run `main.py`

## Note for sending mail via gmail

gmail blocks this scripted mail send behavior, to allow this go to Google Account Setting -> Security -> Less Secure App Access -> Turn On

## To Do
- Gmail API [ ] 
