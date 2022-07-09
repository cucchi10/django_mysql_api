const API= "http://127.0.0.1:8000/api/companies/";

let companies = null;

const getCompanies=async()=>{
    const rest=await fetch(API);
    const data=await rest.json();
    //console.log(data);
    companies = data.companies;
}

window.addEventListener("load", function() {
    getCompanies();
});


//levantar server con python
//python -m http.server

//con nodejs
//static
