const url = "http://127.0.0.1:8000";

const deleteCORS = {
  mode: 'no-cors',
  headers: {
      "Access-Control-Allow-Origin" : "*", 
      "Access-Control-Allow-Credentials" : true 
    }
}

async function getCurrentCityFunc(){
  await fetch(`${url}/getCurrentCity`, deleteCORS)
}

async function getAllCityDataFunc(){
  await fetch(`${url}/getAllCityData`, deleteCORS)
}

console.log(getAllCityDataFunc());

getCurrentCityFunc();