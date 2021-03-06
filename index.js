import default greeting from 'imports/out';

const saludo = "Holaa";
var alertar = (e, ...nombres) => {
	console.log(e);
	alert(saludo);
	nombres.forEach((nombre) => {
	  greeting(nombre);
	});
};
var chargeEvents = () => {
	document.getElementsByName('encabezado')[0].addEventListener('click', () => {
		alertar('Juan', 'Felipe', 'Rodríguez');
	});
};
document.addEventListener('load', chargeEvents());
