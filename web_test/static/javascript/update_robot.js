/*
データの更新
*/
const form = document.getElementById("form")
const submitButton = document.getElementById("submit-button")

submitButton.onclick = () => {
    const robot_id = document.getElementById("robot-id").innerText
    if (robot_id == ""){
        alert("対象がドロップダウンリストで選択されていません")
        return
    }

    const formData = new FormData(form)
    const action = form.getAttribute("action") + "/" + robot_id
    const data = Object.fromEntries(formData.entries())

    console.log(data)
    console.log(action)

    const options = {
        method: 'PUT',
        headers: {
            'Content-Type':'application/json',
        },
        body: JSON.stringify(data),
    }
    fetch(action, options).then((e) => {
        if(e.status === 200){
            alert("送信しました")
            func1()
            return
        }
        alert("送信できませんでした。")
    })

}

/*
ドロップダウンリストの更新
*/

// function get_robots(){
//     var robots = new Array()
//     robots.push({'id':1, name:"tanaka", version:"0.0.0"})
//     robots.push({'id':2, name:"nakamura", version:"0.0.0"})
//     return robots
// }
// const robots = get_robots()

const name2robot = new Map()
function set_name2robot(robots){
    let L = selectList.options.length - 1
    for (let i=L; i >= 1;i--){
        selectList.remove(i)
    }

    for (robot of robots){
        name2robot.set(robot.name, robot)
    }
    console.log(name2robot)
}

const selectList = document.getElementById("select")
function set_selectList(robots){
    selectList.options.langth = 0
    for (let i in robots){
        var option = new Option(robots[i].name, Number(i)+1)
        selectList.add(option)
    }
}

const action = "/api/robots"
const func1 = async () => {
    let res = await fetch(action)
    let json = await res.json()
    console.log(json)

    set_name2robot(json)
    set_selectList(json)
}
func1()

/*
ドロップダウンリストの選択完了時に情報を更新
*/
selectList.addEventListener("change", (e) => {
    const label_id = document.getElementById("robot-id")
    const label_name = document.getElementById("robot-name")
    const label_version = document.getElementById("robot-version")

    const form_robot_name = document.getElementById("form-robot-name")
    const form_robot_version = document.getElementById("form-robot-version")

    if (e.target.selectedIndex == 0){
        label_id.innerText = ""
        label_name.innerText = ""
        label_version.innerText = ""
        form_robot_name.value = ""
        form_robot_version.value = ""
    }
    else{
        console.log(e.target.options[e.target.selectedIndex])
        var name = e.target.options[e.target.selectedIndex].label
        robot = name2robot.get(name)

        label_id.innerText = `${robot['id']}`
        label_name.innerText = `${robot['name']}`
        label_version.innerText = `${robot['version']}`
        form_robot_name.value = `${robot['name']}`
        form_robot_version.value = `${robot['version']}`
    }
});
