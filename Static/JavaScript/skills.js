<script>
    function addSkill(){
        var node = document.createElement("LI");
        var textnode = document.createTextNode("Skill:" + document.getElementById("skill").value + " " +
            "Proficiency:" + document.getElementById("pro").value);
        node.setAttribute("class", "list-group-item");
        node.appendChild(textnode);
        document.getElementById("skills_list").appendChild(node);

        var hiddenField = document.createElement("input");
        hiddenField.setAttribute("type", "hidden");
        hiddenField.setAttribute("name", document.getElementById("skill").value);
        hiddenField.setAttribute("value", document.getElementById("pro").value);
        document.getElementById("send").appendChild(hiddenField);
        console.log(hiddenField.value);
        document.getElementById("new_skill").reset();
    }

