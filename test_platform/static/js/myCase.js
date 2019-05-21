

//初始化 “项目>模块” 二级联动菜单
var SelectInit = function (defaultProjectId, defaultModuleId) {
    var cmbProject = document.getElementById("selectProject");
    var cmbModule = document.getElementById("selectModule");
    var dataList = [];
    console.log("wtf", cmbProject);

    //设置默认选项
    function setDefaultOption(obj, id) {
        for (var i = 0; i < obj.options.length; i++) {
            if (obj.options[i].value == id) {
                obj.selectedIndex = i;
                return;
            }
        }
    }

    //创建下拉选项
    function addOption(cmb, obj) {
        var option = document.createElement("option");
        cmb.options.add(option);
        option.innerHTML = obj.name;
        option.value = obj.id;
    }

    //改变项目
    function changeProject() {
        cmbModule.options.length = 0;
        if (cmbProject.selectedIndex == -1) {
            return;
        }
        var pid = cmbProject.options[cmbProject.selectedIndex].value;
        
        for (let i = 0; i < dataList.length; i++) {
            if(dataList[i].id == pid) {
                let modules = dataList[i].moduleList;
                for(let j=0; j< modules.length; j++){
                    addOption(cmbModule, modules[j]);
                }
            }
            
        }

        setDefaultOption(cmbModule, defaultModuleId);
    }

    function getSelectData() {
        // 调用获取select数据列表
        $.get("/testcase/get_select_data", {}, function (resp) {
            if (resp.status === 10200) {
                dataList = resp.data;
                //遍历项目
                for (var i = 0; i < dataList.length; i++) {
                    addOption(cmbProject, dataList[i]);
                }

                setDefaultOption(cmbProject, defaultProjectId);
                changeProject();
                cmbProject.onchange = changeProject;
            }

            setDefaultOption(cmbProject, defaultProjectId);

        });
    }

    // 调用getSelectData函数
    getSelectData();

};

/////////接口需要的数据格式////////////////////
// {
//     "id": 2,
//     "name": "新项目BBB",
//     "moduleList": [
//        {
//         "id": 4,
//         "name": "模块AA"
//        },
//        {
//         "id": 5,
//         "name": "模块BB"
//        }
//     ]
// },
////////////////////////////////////////////


//创建下拉选项 -->废弃
function cmbAddOption(cmb, obj) {
    let option = document.createElement("option");
    cmb.options.add(option);
    option.innerHTML = obj.name;
    option.value = obj.id;
}

//清理下拉选项 -->废弃
function clearOption(cmb) {
    for (let i = 0; i <= cmb.length; i++) {
        cmb.options.remove(cmb[i]);
    }
}


// 获取项目列表 -->废弃
var ProjectInit = function (_cmbProject) {
    var cmbProject = document.getElementById(_cmbProject);

    console.log("初始化项目...");

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

    //ModuleInit(1);
    

};


// 获取某一个项目的模块列表 -->废弃
var ModuleInit = function (_cmbModule, pid) {
    console.log("初始化模块...", pid);

    var cmbModule = document.getElementById(_cmbModule);

    function getModuleListInfo() {
        $.post("/module/get_module_list/", {
            "pid": pid
        }, function (resp) {
            if (resp.status == 10200) {
                console.log("6666666", resp.data);
                let dataList = resp.data;
                clearOption(cmbModule);
                for (let i = 0; i < dataList.length; i++) {
                    cmbAddOption(cmbModule, dataList[i]);
                }
                //$("#module_name").selectpicker("refresh");
            } else {
                window.alert(resp.message);
            }
        });

    }

    // 调用getCaseListInfo函数
    getModuleListInfo();

};



//获取用例信息
var TestCaseInit = function () {

    var url = document.location;
    var cid =  url.pathname.split("/")[3];

    $.post("/testcase/get_case_info",
    {
        cid: cid,
    },
    function (resp, status) {
        console.log("返回的结果", resp.data);
        var result = resp.data;

        //请求URL
        document.querySelector("#req_url").value = resp.data.url;
        
        //请求方法
        if (result.method == 1){
            document.querySelector("#get").setAttribute("checked", "");
        }else if (result.method == 2) {
            document.querySelector("#post").setAttribute("checked", "");
        }else if (result.method == 3){
            document.querySelector("#put").setAttribute("checked", "");
        } else if (result.method == 4){
            document.querySelector("#delete").setAttribute("checked", "");
        }

        //请求头
        document.querySelector("#header").value = result.header;

        //请求参数类型
        if (result.parameter_type == 1) {
            document.querySelector("#form").setAttribute("checked", "");
        }
        else if (result.parameter_type == 2) {
            document.querySelector("#json").setAttribute("checked", "");
        }

        //请求参数的值
        document.querySelector("#parameter").value = result.parameter_body;
        
        //断言的类型
        if (result.assert_type == 1) {
            document.querySelector("#contains").setAttribute("checked", "");
        }
        else if (result.assert_type == 2) {
            document.querySelector("#mathches").setAttribute("checked", "");
        }

        //断言的值
        document.querySelector("#assert").value = result.assert_text;

        //用例的名称
        document.querySelector("#case_name").value = result.name;

        // 初始化菜单
        SelectInit(result.project_id, result.module_id);

        // 初始化用例所属项目
        // let options = document.querySelectorAll("#project_name > option");
        // for (let i = 0; i < options.length; i++) {
        //     let optionValue = options[i].value;
        //     if (optionValue == result.project_id) {
        //         options[i].selected = true;
        //         //let optionName = options[i].text;
        //         //document.querySelectorAll(".filter-option-inner-inner")[0].innerText = optionName;
        //     }
        // }


        // ModuleInit("module_name", result.project_id);
        // //location.replace(location.href);

        // SelectModule(result.module_id);
    });

    


    //SelectModule(result.module_id);
    
}
