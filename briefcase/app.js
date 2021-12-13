const express = require('express')
const bodyParser = require("body-parser")
const app = express()
const port = 8091

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.post('/briefcase-verify', (req, res) => {
    console.log(req.body.pin);
    if (req.body.pin == '666') {
        res.send("valid");
    } else {
        res.send("invalid");
    }
});
    
app.listen(port, () => console.log(`Briefcase app listening on port ${port}!`))
