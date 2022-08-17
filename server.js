const express = require('express')
const app = express()
const bodyParser = require('body-parser')
const ejs = require('ejs')
const mongoose = require('mongoose')
const spawn = require("child_process").spawn;
const fs = require('fs')
const multer = require('multer')

var upload = multer({ dest: 'uploads/' })

app.set('view engine', 'ejs');
app.use(express.static("public"))
app.use(bodyParser.urlencoded({ extended: true }))

app.get("/", function (req, res) {
    res.render("home")
})

app.post("/analyze", upload.single('chat_file'), function (req, res, next) {

    fs.readFile(req.file.path, 'utf-8', function (err, data) {
        if (err) {
            console.log(err)
        }
        else {
            var process = spawn('python', ["Analyser/main.py", data]);
            process.stdout.on('data', (data) => {
                console.log(data.toString())
                fs.readFile("files/info.txt",'utf-8',function(err,data)
                {
                    res.render('analyzed',{data:data})
                })
               
            })
        }
    });
})


let port=process.env.PORT;
if(port=="" || port==null){
    port=3000;
}

app.listen(port,function(){
    console.log("Server Running Up")
})