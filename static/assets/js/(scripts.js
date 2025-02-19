// Alternar entre Login e Cadastro
document.getElementById('toggleSignup').addEventListener('click', (e) => {
  e.preventDefault();
  document.getElementById('loginForm').classList.add('hidden');
  document.getElementById('signupForm').classList.remove('hidden');
});

document.getElementById('toggleLogin').addEventListener('click', (e) => {
  e.preventDefault();
  document.getElementById('signupForm').classList.add('hidden');
  document.getElementById('loginForm').classList.remove('hidden');
});

// Simulação de envio de dados
const forms = document.querySelectorAll('.form');
forms.forEach(form => {
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const button = form.querySelector('.btn');
    button.classList.add('loading');

    // Simulação de requisição assíncrona
    setTimeout(() => {
      button.classList.remove('loading');
      if (form.id === 'loginForm') {
        alert('Login realizado com sucesso!');
      } else {
        alert('Cadastro realizado com sucesso! Bem-vindo ao Condofácil!');
      }
    }, 2000); // Simula 2 segundos de processamento
  });
});