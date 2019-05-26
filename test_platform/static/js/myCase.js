

//初始化 “项目>模块” 二级联动菜单
var SelectInit = function (defaultProjectId, defaultModuleId) {
    var cmbProject = document.getElementById("selectProject");
    var cmbModule = document.getElementById("selectModule");

    var dataList = [];
    
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
        console.log("项目默认选项的索引", cmbProject.selectedIndex);
        var pid = cmbProject.options[cmbProject.selectedIndex].value;
        console.log("这个才是真的项目id", pid);

        for (let i = 0; i < dataList.length; i++) {
            if(dataList[i].id == pid) {
                let modules = dataList[i].moduleList;
                console.log("对应的模块列表", modules);
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
                console.log("想要的数据格式-->", dataList);
                //遍历项目
                for (var i = 0; i < dataList.length; i++) {
                    console.log("每一个项目的数据", dataList[i]);
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

    });

}
