const express = require('express');
const PORT = process.env.PORT || 8000;

const app = express();

app.get('/', (req, res) => {
  res.send("### Response from Express Server ###")
});

app.listen(PORT, () => {
  console.log(`Listening on port ${PORT}`)
})