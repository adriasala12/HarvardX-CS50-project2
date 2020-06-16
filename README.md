# Project 2

Web Programming with Python and JavaScript

## Summary

The website allows the user to identify herself with a name, create channels, and send and receive messages in these channels.

## HTML Files
### index.html
The website firs asks the user to enter a display name. Once the user enters the name and submits the form, she is redirected to the home page. This name is saved in the session object until the user presses the Log Out button in the home page. If the user closes the webpage and access this page again, she is automatically redirected to the home screen or to the last channel she visitted before closing the website.

### home.html
This is the home page of the website, the page that displays once the user logs in. In this page, the user can see a welcome message and a log out button to remove the name from the session object.
Then a list of channels is displayed. If there are no channels created yet, a message is displayed instead. The user can create channels by clicking the corresponding button, which shows a form to create a new channel.
When a new channel is created it is displayed in the channels list. The user can click it to enter the channel.

### channel.html
This page is a template for each channel, which displays the channel name, a home button to go back to the home screen and a delete button to remove the channel. The user can see the last 100 messages sent to the channel, as well as sending new messages using the form below.

## JavaScript Files
### manageChannels.js
This file handles the client-side of the function that allows the user to create a new channel. When creating a new channel, if the name is empty or repeated, an alert is displayed to the user. It also displays the form for adding a new channel when the "add channel" button is pressed and dismisses the form on submit.

### messages.js
This file contains the socket.io code for sending and receiving new messages. When a message is sent, it emmits the message to the backend. When the message is broadcasted back to the frontend, it adds it to the messages list shown onscreen. If this list exceeds the limit of 100 messages, the old messages are removed as new messages are sent/received.
Finally, we find a function that makes the message form to submit when the return key is pressed.

