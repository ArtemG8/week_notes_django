window.onload = function() {
    var inputFields = document.getElementsByTagName('input');
    for (var i = 0; i < inputFields.length; i++) {
        inputFields[i].removeAttribute('required');
        inputFields[i].removeAttribute('maxlength');
        inputFields[i].removeAttribute('minlength');
    }
};

//window.onload = function() {
//  var nameInput = document.getElementById('id_name');
//  var surnameInput = document.getElementById('id_surname');
//  var nameError = document.createElement('div');
//  var surnameError = document.createElement('div');
//
//  nameInput.addEventListener('input', function() {
//    var validName = nameInput.value.replace(/[^a-zA-Zа-яА-Я]/g, '');
//    if (nameInput.value !== validName) {
//      nameError.innerHTML = 'Можно вводить только буквы';
//      nameError.classList.add('error-message');
//      if (!nameInput.parentNode.contains(nameError)) {
//        nameInput.parentNode.appendChild(nameError);
//      }
//    } else {
//      nameError.innerHTML = '';
//      nameError.classList.remove('error-message');
//    }
//    nameInput.value = validName;
//  });
//
//  surnameInput.addEventListener('input', function() {
//    var validSurname = surnameInput.value.replace(/[^a-zA-Zа-яА-Я]/g, '');
//    if (surnameInput.value !== validSurname) {
//      surnameError.innerHTML = 'Можно вводить только буквы';
//      surnameError.classList.add('error-message');
//      if (!surnameInput.parentNode.contains(surnameError)) {
//        surnameInput.parentNode.appendChild(surnameError);
//      }
//    } else {
//      surnameError.innerHTML = '';
//      surnameError.classList.remove('error-message');
//    }
//    surnameInput.value = validSurname;
//  });
//};
