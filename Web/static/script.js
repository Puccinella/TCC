async function carregarLog() {
  const prontuario = document.getElementById('Prontuario').value.trim();
  const data = document.getElementById('filtroData').value;

  const params = new URLSearchParams();
  if (prontuario) params.append('prontuario', prontuario);
  if (data) params.append('data', data);

  const resposta = await fetch('/api/log?' + params.toString());
  const registros = await resposta.json();

  const tbody = document.querySelector('table tbody');
  tbody.innerHTML = '';

  if (registros.length === 0) {
    tbody.innerHTML = `
      <tr>
        <td colspan="5" class="text-center text-muted">Nenhum registro encontrado</td>
      </tr>
    `;
    return;
  }

  registros.forEach(registro => {
    const dataHora = new Date(registro.data_hora);
    const dataFormatada = dataHora.toLocaleDateString('pt-BR');
    const horaFormatada = dataHora.toLocaleTimeString('pt-BR');

    const linha = document.createElement('tr');
    linha.innerHTML = `
      <th scope="row">${registro.numero}</th>
      <td>${registro.prontuario}</td>
      <td>${dataFormatada}</td>
      <td>${horaFormatada}</td>
      <td>${registro.status}</td>
    `;
    
    tbody.appendChild(linha);
  });
}

document.getElementById('btnFiltrar').addEventListener('click', carregarLog);

document.getElementById('btnLimpar').addEventListener('click', () => {
  document.getElementById('Prontuario').value = '';
  document.getElementById('filtroData').value = '';
  carregarLog();
});

carregarLog();