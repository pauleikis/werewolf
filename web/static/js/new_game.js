(function(){
    var app = angular.module("werewolfGame", []);

    app.controller("RoleCtrl", function($scope){

        $scope.roles = {};
        $scope.role_selection = [];

        $scope.$watch('roles', function (nv) {
            var role_selection = [];
            for (var key in nv) {
                if (key) {
                    role_selection.push(key);
                }
            }
            $scope.role_selection = role_selection;
        }, true);

        Sortable.create(allRoles, {
            group: "roles",
        });

        Sortable.create(selectedRoles, {
            group: "roles",
        });
    });
})();