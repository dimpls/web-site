document.addEventListener('DOMContentLoaded', function() {

    // инициализация календаря
    var calendarBody = document.querySelector('.calendar-body');
    var currentDate = new Date();
    var currentMonth = currentDate.getMonth();
    var currentYear = currentDate.getFullYear();
    var daysInMonth = new Date(currentYear, currentMonth + 1, 0).getDate();
    var firstDayOfMonth = new Date(currentYear, currentMonth, 1).getDay();
    var lastDayOfPrevMonth = new Date(currentYear, currentMonth, 0).getDate();
    var lastDayOfPrevMonthOffset = new Date(currentYear, currentMonth, 0).getDay();
    var prevSelectedDay = null;
    
    // заполнение пустых ячеек предыдущего месяца
    for (var i = lastDayOfPrevMonthOffset; i > 0; i--) {
      var prevDay = document.createElement('div');
      prevDay.className = 'calendar-day calendar-day--prev-month';
      prevDay.innerHTML = lastDayOfPrevMonth - i + 1;
      calendarBody.appendChild(prevDay);
    }
    
    // заполнение календаря
    for (var i = 1; i <= daysInMonth; i++) {
        var day = document.createElement('div');
        day.className = 'calendar-day';
        day.innerHTML = i;
        day.addEventListener('click', function() {
          if (prevSelectedDay) {
            prevSelectedDay.classList.remove('calendar-day--selected');
            prevSelectedDay.style.backgroundColor = ''; // вернуть цвет фона в исходное состояние
          }
          this.classList.add('calendar-day--selected');
          this.style.backgroundColor = 'lightblue';
          prevSelectedDay = this; // сохранить ссылку на текущую ячейку
          showModal(currentMonth + 1, this.innerHTML);
        });
        calendarBody.appendChild(day);
    }

    var submitButton = document.querySelector('.calendar-submit');
    submitButton.addEventListener('click', function() {
        var selectedTime = document.querySelector('#time').value;
        var selectedMaster = document.querySelector('#master').value;
        var selectedDate = document.querySelector('.calendar-day--selected');
        if (selectedDate) {
          selectedDate = selectedDate.innerHTML;
        } else {
          selectedDate = '';
        }
    console.log('Запись на ' + selectedDate + '.' + (currentMonth + 1) + '.' + currentYear + ' в ' + selectedTime + ' к мастеру ' + selectedMaster + ' подтверждена');
  });
  
  
});

function showModal(month, day) {
  console.log('Выбрана дата: ' + month + '/' + day);
}