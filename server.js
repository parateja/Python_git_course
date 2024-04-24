const express=require('express');
const app=express();
const mongoose=require('mongoose');
const {MongoClient}=require('mongodb')
app.listen(5000, ()=>{console.log('connection listened on 50000')})
mongoose.set('strictQuery', true);
const url="mongodb://localhost:27017";
const client=new MongoClient(url);
const database='college';
async function getData(){
 let result =await client.connect();
 db=result.db(database);
 collection=db.collection('staffdetails');
 let data=await collection.find({}).toArray();
 console.log(data);
}
getData();
