//Java Script object notation =>Format

var Person ={
    Name:"Hareshan",
    School:"AGS",
    Age:13,
}

const PersonJson = JSON.stringify(Person)

const RecivedJson = JSON.parse(PersonJson)

console.log(RecivedJson.Name)

console.log(RecivedJson.School)


console.log(RecivedJson.Age)