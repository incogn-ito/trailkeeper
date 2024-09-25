const dateInput = document.getElementById('id_target_date')

const picker = MCDatepicker.create({
  el: '#id_target_date',
  dateFormat: 'yyyy-mm-dd',
  closeOnBlur: true,
  selectedDate: new Date(),
})

dateInput.addEventListener("click", () => {
  picker.open()
})