const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

// Parse JSON bodies for POST requests
app.use(express.json());

// Set up the Webhook Path and Verify Token from environment variables
// Defaults to /webhook and 'my_custom_verify_token' if not provided
const WEBHOOK_PATH = process.env.WEBHOOK_PATH || '/webhook';
const VERIFY_TOKEN = process.env.VERIFY_TOKEN || 'my_custom_verify_token';

// Adds support for GET requests to our webhook (Meta Verification)
app.get(WEBHOOK_PATH, (req, res) => {
  // Parse the query params sent by Meta
  let mode = req.query["hub.mode"];
  let token = req.query["hub.verify_token"];
  let challenge = req.query["hub.challenge"];

  // Check if a token and mode is in the query string of the request
  if (mode && token) {
    // Check the mode and token sent is correct
    if (mode === "subscribe" && token === VERIFY_TOKEN) {
      // Respond with the challenge token from the request
      console.log("WEBHOOK_VERIFIED");
      res.status(200).send(challenge);
    } else {
      // Respond with '403 Forbidden' if verify tokens do not match
      console.log("WEBHOOK_VERIFICATION_FAILED: Tokens do not match");
      res.sendStatus(403);
    }
  } else {
    // If hub.mode or hub.verify_token are missing
    res.sendStatus(400);
  }
});

// Endpoint to receive actual webhook event notifications
app.post(WEBHOOK_PATH, (req, res) => {
  let body = req.body;

  console.log(`\n--- Received webhook payload ---`);
  console.dir(body, { depth: null });
  console.log(`--------------------------------\n`);
  
  // Return a '200 OK' response to all requests to acknowledge receipt
  // Meta expects a 200 OK response within 20 seconds.
  res.status(200).send('EVENT_RECEIVED');
});

// Start the server
app.listen(port, () => {
  console.log(`\u2705 Server is running on port ${port}`);
  console.log(`\u{1F517} Webhook verification endpoint: GET http://localhost:${port}${WEBHOOK_PATH}`);
  console.log(`\u{1F4E7} Webhook event endpoint: POST http://localhost:${port}${WEBHOOK_PATH}`);
  console.log(`\u{1F511} Expected Verify Token: ${VERIFY_TOKEN}`);
});
