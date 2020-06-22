const typeWriter = () => {
  const tags = ['coding', 'python','javascript', 'django', 'flask', 'tech'];
  let count = 0;
  let tagIndex = 0;
  let currentTag = '';
  let letter = '';

  (function type() {

    if(count === tags.length) {
      count = 0;
    }

    currentTag = tags[count];
    letter = currentTag.slice(0, ++tagIndex)

    document.querySelector('.typing').textContent = letter;
    if(letter.length === currentTag.length) {
      count++
      tagIndex = 0;
    }
    setTimeout(type, 350);

  }());
} 

typeWriter();