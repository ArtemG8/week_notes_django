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

        function confirmDelete(todoId) {
            if (confirm('Вы уверены, что хотите удалить эту задачу?')) {
                const form = document.createElement('form');
                form.method = 'post';
                form.action = ''; // Отправка на текущий URL
                form.innerHTML = `<input type="hidden" name="todo_id" value="${todoId}"><input type="hidden" name="delete" value="true">`;
                document.body.appendChild(form);
                form.submit();
            }
        }

