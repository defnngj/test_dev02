// 获取项目列表
var ProjectInit = function (_cmbProject) {
    var cmbProject = document.getElementById(_cmbProject);

    //创建下拉选项
    function cmbAddOption(cmb, obj) {
        let option = document.createElement("option");
        cmb.options.add(option);
        option.innerHTML = obj.name;
        option.value = obj.id;
    }

    function getProjectListInfo() {
        // 获取某个用例的信息
        $.get("/project/get_project_list/", {}, function (resp) {
            if (resp.status == 10200) {
                console.log(resp.data);
                let dataList = resp.data;
                for (let i = 0; i < dataList.length; i++) {
                    cmbAddOption(cmbProject, dataList[i]);
                }
            } else {
                window.alert(resp.message);
            }
        });
    }

    // 调用getCaseListInfo函数
    getProjectListInfo();

};