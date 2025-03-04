// Добавляем анимацию при изменении статуса
        document.querySelectorAll('form').forEach(form => {
            form.addEventListener('submit', function(e) {
                const checkbox = this.querySelector('.custom-checkbox');
                checkbox.classList.toggle('checked');

                const statusText = this.querySelector('.status-text');
                statusText.textContent = checkbox.classList.contains('checked')
                    ? 'Выполнено'
                    : 'Отметить как выполненное';
            });
        });








