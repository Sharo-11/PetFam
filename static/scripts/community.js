<<<<<<< HEAD
document.getElementById('commentForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent form from submitting

    const username = document.getElementById('username').value;
    const comment = document.getElementById('comment').value;
    const isAnonymous = document.getElementById('anonymous').checked;

    // Display the comment
    const commentsList = document.getElementById('commentsList');
    const commentDiv = document.createElement('div');
    commentDiv.className = 'comment';
    commentDiv.textContent = `${isAnonymous ? 'Anonymous' : username || 'Anonymous'}: ${comment}`;
    
    commentsList.appendChild(commentDiv);

    // Clear the form
    document.getElementById('username').value = '';
    document.getElementById('comment').value = '';
    document.getElementById('anonymous').checked = false;
});
=======
document.getElementById('commentForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent form from submitting

    const username = document.getElementById('username').value;
    const comment = document.getElementById('comment').value;
    const isAnonymous = document.getElementById('anonymous').checked;

    // Display the comment
    const commentsList = document.getElementById('commentsList');
    const commentDiv = document.createElement('div');
    commentDiv.className = 'comment';
    commentDiv.textContent = `${isAnonymous ? 'Anonymous' : username || 'Anonymous'}: ${comment}`;
    
    commentsList.appendChild(commentDiv);

    // Clear the form
    document.getElementById('username').value = '';
    document.getElementById('comment').value = '';
    document.getElementById('anonymous').checked = false;
});
>>>>>>> a0501fb2aecda9230a9329b19ddab254e2aba35d
