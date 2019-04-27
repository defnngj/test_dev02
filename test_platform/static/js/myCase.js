
// 获取项目列表
var PorjectInit = function (_cmbProject) {
	var cmbProject = document.getElementById(_cmbProject);
	var options = "";

	//创建下拉选项
	function cmbAddOption(cmb, porject_obj) {
		console.log(porject_obj);
		var option = document.createElement("option");	
		cmb.options.add(option);
		option.innerHTML = porject_obj.name;
		option.value = porject_obj.id;
	}

	function getProjectListInfo() {
		// 获取某个用例的信息
		$.get("/project/get_project_list/", {}, function (resp) {
			if (resp.status == 10200) {
				console.log(resp.data);
				let dataList = resp.data;
				for (var i = 0; i < dataList.length; i++) {
					cmbAddOption(cmbProject, dataList[i]);
				}

				//cmbSelect(cmbProject, defaultProject);

				// let cases = resp.data;
				// for (let i = 0; i < cases.length; i++) {
				// 	let option = '<input type="checkbox" name="' + cases[i].name
				// 		+ '" value="' + cases[i].id + '" /> ' + cases[i].name + '<br>'

				// 	options = options + option;

				// }
				// let devCaseList = document.querySelector(".caseList");
				// devCaseList.innerHTML = options;

			} else {
				window.alert(resp.message);
			}
			//$("#result").html(resp);
		});
	}

	// 调用getCaseListInfo函数
	getProjectListInfo();

};