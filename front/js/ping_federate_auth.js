(function() {
    'use strict';

    this.taigaContribPlugins = this.taigaContribPlugins || [];

    var pingFederateAuthInfo = {
        slug: "pingfederate-auth",
        name: "Ping Federate Auth",
        type: "auth",
        module: "taigaContrib.pingfederateAuth",
        template: "contrib/ping_federate_auth"
    };

    this.taigaContribPlugins.push(pingFederateAuthInfo);

    var module = angular.module('taigaContrib.pingfederateAuth', []);

    var PingFederateLoginButtonDirective = function(
        $window,
        $params,
        $location,
        $config,
        $events,
        $confirm,
        $auth,
        $navUrls,
        $loader
    ) {
        /**
         *
         */
        var link = function($scope, $el, $attrs) {
        
            var clientId = $config.get("", null);
            var loginOnSuccess = function(response) {
                var nextUrl = $navUrls.resolve("home");
                if (
                    $params.next &&
                    $params.next !== $navUrls.resolve("login")
                ) {
                    nextUrl = $params.next;
                }

                $events.setupConnection();
                $location.search("next", null);
                $location.search("REF", null);
                $location.search("TargetResource", null);

                var redirectToUri = $location.url(nextUrl).absUrl();
                return $window.location.href = redirectToUri;

            };
            
            var loginOnError = function(response) {
                $location.search("TargetResource", null);
                $location.search("REF", null);
                $loader.pageLoaded();
                if (response.data.error_message) {
                    return $confirm.notify(
                        "light-error",
                        response.data.error_message
                    );
                }
                return $confirm.notify(
                    "light-error",
                    "Our Oompa Loompas have not been able to get you credentials from Ping Federate."
                );
            };

            var loginWithPingFederateAccount = function() {
                var targetResource = $params.TargetResource;
                var ref = $params.REF;

                if (!(targetResource && ref)) {
                    return;
                }
                $loader.start();
                var data = {
                    targetResource: targetResource,
                    REF: ref
                };
                return $auth.
                    login(data, "pingfederate").
                    then(
                        loginOnSuccess,
                        loginOnError
                    )
                ;
            };
      
            loginWithPingFederateAccount();
            $el.on(
                "click",
                ".button-auth",
                function(event) {
                    var redirectToUri = $location.url($location.path()).absUrl();

                    var PING_FEDERATE_AUTH_SERVICE_URL = $config.get("pingfederateAuthServiceURL", null);
                    var PING_FEDERATE_TARGET_RESOURCE = $config.get("pingfederateTargetResource", null);
                    var url = "" + PING_FEDERATE_AUTH_SERVICE_URL +
                        "/pf/adapter2adapter" +
                        "?TargetResource=" + PING_FEDERATE_TARGET_RESOURCE
                    ;
                    console.log(redirectToUri);

                    return $window.location.href = url;
                }
            );

            return $scope.$on(
                "$destroy",
                function() { return $el.off(); }
            );
        };

        return {
            link: link,
            restrict: "EA",
            template: ""
        }
    };

    module.directive(
        "tgPingFederateLoginButton",
        [
            "$window",
            '$routeParams',
            "$tgLocation",
            "$tgConfig",
            "$tgEvents",
            "$tgConfirm",
            "$tgAuth",
            "$tgNavUrls",
            "tgLoader",
            PingFederateLoginButtonDirective
        ]
    );

    module.run([
        '$templateCache',
        function($templateCache) {
            return $templateCache.put(
                'contrib/ping_federate_auth',
                '<div tg-ping-federate-login-button="tg-ping-federate-login-button">' +
                    '<a href="" title="Enter with your ping federate account" class="button button-auth">'+
                        '<img src="images/contrib/google-logo.png"/>' + 
                        '<span>Login with Ping Federate</span>' +
                    '</a>' + 
                '</div>'
            );
        }
    ]);

}).call(this);
