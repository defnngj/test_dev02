//创建下拉选项
function cmbAddOption(cmb, obj) {
    let option = document.createElement("option");
    cmb.options.add(option);
    option.innerHTML = obj.name;
    option.value = obj.id;
}

//清理下拉选项
function clearOption(cmb) {
    for (let i = 0; i <= cmb.length; i++) {
        cmb.options.remove(cmb[i]);
    }
}


// 获取项目列表
var ProjectInit = function (_cmbProject) {
    var cmbProject = document.getElementById(_cmbProject);

    function getProjectListInfo() {
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


// 获取某一个项目的模块列表
var ModuleInit = function (_cmbModule, pid) {
    var cmbModule = document.getElementById(_cmbModule);

    function getModuleListInfo() {
        $.post("/module/get_module_list/", {
            "pid": pid
        }, function (resp) {
            if (resp.status == 10200) {
                console.log(resp.data);
                let dataList = resp.data;
                clearOption(cmbModule);
                for (let i = 0; i < dataList.length; i++) {
                    cmbAddOption(cmbModule, dataList[i]);
                }
                $("#module_name").selectpicker("refresh");
            } else {
                window.alert(resp.message);
            }
        });
    }

    // 调用getCaseListInfo函数
    getModuleListInfo();

};