document.addEventListener('DOMContentLoaded', function() {
    console.log("DOM loaded");
    lock_btns = document.getElementsByClassName('lock-btn');
    Array.from(lock_btns).forEach(btn => {
        btn.addEventListener('click', () => {
            note_id = btn.id.replace(/^\D+/g, '')
            console.log(`note id ${note_id}`);
            fetch("/lock/" + note_id, {
                    method: 'POST'
                })
                .then(res => res.json())
                .then(resjson => {
                    console.log(resjson);
                    window.location = 'http://127.0.0.1:8000/allnote'
                })
        })
    });
    unlock_btns = document.getElementsByClassName('unlock-btn');
    Array.from(unlock_btns).forEach(btn => {
        btn.addEventListener('click', () => {
            note_id = btn.id.replace(/^\D+/g, '')
            console.log(`note id ${note_id}`);
            passwordField = document.getElementById('password-unlock-' + note_id)
            console.log(`password ${passwordField.value}`);
            fetch("/unlock/" + note_id, {
                    method: 'POST',
                    body: JSON.stringify({
                        password: passwordField.value
                    })
                })
                .then(res => {
                    if (res.status == 400) {
                        console.log('error');
                        return true
                    }

                    return false
                })
                .then(hasError => {
                    if (hasError) {
                        alert("Your password is incorrect. Please try again.")
                    } else {
                        window.location = 'http://127.0.0.1:8000/allnote'
                    }
                })


        })
    })
})