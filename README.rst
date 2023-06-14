Omkar Temp Mail
===============

Omkar Temporary Email offers a convenient solution for receiving
temporary emails. It is particularly useful for automated tasks that
require email verification during account creation.

Getting Started
---------------

To get started with Omkar Temp Mail install ``omkar-temp-mail`` using
the following command:

.. code:: bash

   python -m pip install omkar-temp-mail

Usage
-----

1. ``get_domains`` Returns a list of available domain options for
   generating temporary email addresses.

.. code:: python

   from omkar_temp_mail import TempMail

   domains = TempMail.get_domains()
   print(domains) # prints ['1secmail.com', '1secmail.org', '1secmail.net', 'kzccv.com', 'qiott.com', 'wuuvo.com', 'icznn.com', 'ezztt.com']

2. ``get_email_link(email)``

Get’s the first link from the most recent email message received in the
given email address.

.. code:: python

   from omkar_temp_mail import TempMail

   email = "shyam@1secmail.com"
   link = TempMail.get_email_link(email)
   print(link) 

3. ``get_body(email)``

Get’s the content (text or HTML) from the most recent email message
received in the given email address.

.. code:: python

   from omkar_temp_mail import TempMail

   email = "shyam@1secmail.com"
   body = TempMail.get_body(email)
   print(body) 

4. ``deleteMailbox(email)``

Deletes the mailbox associated with the provided email address.

.. code:: python

   from omkar_temp_mail import TempMail

   email = "shyam@1secmail.com"
   TempMail.deleteMailbox(email)

5. ``get_email_link_and_delete_mailbox(email)``

Combines the functionality of ``get_email_link`` and
``deleteMailbox(email)``. It first retrieves the first link from the
most recent email and then deletes the mailbox, returning the link.

.. code:: python

   from omkar_temp_mail import TempMail

   email = "shyam@1secmail.com"
   link = TempMail.get_email_link_and_delete_mailbox(email)
   print("Link:", link)

If my code helped you in generating Temporary Email, please take a moment to `star the repository <https://github.com/omkarcloud/omkar-temp-mail>`__. Your act of starring will help developers in discovering our Repository and contribute towards helping fellow developers in their automation tasks. Dhanyawad 🙏! Vande Mataram!
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
