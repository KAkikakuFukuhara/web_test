const form = document.getElementById("form")
const submitButton = document.getElementById("submit-button")

submitButton.onclick = () => {
    const formData = new FormData(form)
    const action = form.getAttribute("action")
    const data = Object.fromEntries(formData.entries())

    console.log(data)

    const options = {
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
        },
        body: JSON.stringify(data),
    }
    fetch(action, options).then((e) => {
        if(e.status === 200){
            alert("送信しました")
            return
        }
        alert("送信できませんでした。")
    })
}