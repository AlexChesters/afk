# AFK

Hack week project that detects when you move away from your OS X/macOS screen
and locks your screen. Uses
[Amazon Rekognition](https://aws.amazon.com/rekognition/).

# Instructions
## Warning
The program will attempt to take and process a new picture as soon as the
previous one has finished. If you are not careful this could be expensive.
Make sure to check the
[Rekognition pricing](https://aws.amazon.com/rekognition/pricing/) before using.

## Dependencies
* `python` 3.x
* An AWS IAM user authorised to perform Rekognition:CompareFaces

## Usage
1. Place a picture of yourself in `images/me.png`
1. `make install`
1. `make run`
