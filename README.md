# SMB Promotional Chatbot

## Introduction

This project is a simple chatbot and tooling for small and medium-sized businesses (SMBs) to send promotional messages and collect statistics on customer interactions. The chatbot follows a predefined flow, allowing SMBs to send coupons to customers and track the effectiveness of their promotions.

## Project Details

- **Estimated Time**: ~4 hours
- **Testing Philosophy**: Testable code with an emphasis on coding decisions.
- **Architecture**: Simple architecture for quick development.
- **Error Handling**: Graceful handling of errors, including downstream dependencies and timeouts.
- **Strengths**: Aim to showcase my expertise, whether it's in architecture, UX, ML, or other areas.

## Project Flow

### 1. Welcome Message
- The chatbot welcomes the customer with a personalized greeting that includes the customer's name.

### 2. Coupon Message
- Clicking "Yes! Show me coupon" displays the coupon message.
    - Clicking on "Reveal the coupon" acknowledges coupon redemption.
- SMBs can track coupon reveal clicks on the statistics dashboard.

### 3. Thank You Message
- Clicking "No, thanks" sends a thank you message with a customizable image.

### 4. Statistics
- Collect statistics on each button click and customer journey within the flow.
    - E.g., How many customers responded to the first message, saw the second message, or interacted with coupons.
- Visualize collected information for SMBs to analyze.

## Technologies and Tools

- **Webhooks**: Used for communication with messaging platforms (e.g., Facebook Messenger API).
TBD

## Deployment

1. Deployable on a PaaS provider like Heroku or AWS Lambda (serverless).
2. Can also run on a development machine for testing purposes.
3. Aim to use containers to create deployable images.

## Getting Started

To set up the project and run it locally:

1. Clone the repository to your local machine.
2. Follow the deployment instructions in the project's specific README (if available).
3. Install any required dependencies.
4. Configure webhook endpoints for your chosen messaging platform.
5. Run the application and test it with sample interactions.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

Thank you for taking the time to review this project. If you have any questions or need further assistance, please don't hesitate to reach out.
