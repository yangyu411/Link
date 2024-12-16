function sortby(sortType) {
    document.querySelectorAll('.nav-item').forEach(item => {
      if (['all', 'distance', 'score'].includes(item.id) && item.id !== sortType) {
        item.classList = 'nav-item smallitem';
      } else if (item.id === sortType) {
        item.classList = 'nav-item selected smallitem';
      }
    });
    // 发送GET请求
    const xhr = new XMLHttpRequest();
    xhr.open('GET', window.location.href, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({sort: sortType}));
  }

function getonly(){
    document.getElementById("mask").style.display='block';
    document.getElementById("filter").style.display="block";
}

function getonlyback(){
    document.getElementById("mask").style.display='none';
    document.getElementById("filter").style.display="none";
}