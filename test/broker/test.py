#!/usr/bin/env python3

import mosq_test_helper
import ptest

tests = [
    #(ports required, 'path'),
    (1, './01-connect-575314.py'),
    (1, './01-connect-accept-protocol.py'),
    (1, './01-connect-allow-anonymous.py'),
    (1, './01-connect-disconnect-v5.py'),
    (1, './01-connect-global-max-clients.py'),
    (1, './01-connect-global-max-connections.py'),
    (1, './01-connect-max-connections.py'),
    (1, './01-connect-max-keepalive.py'),
    (1, './01-connect-take-over.py'),
    (1, './01-connect-uname-no-password-denied.py'),
    (1, './01-connect-uname-or-anon.py'),
    (1, './01-connect-uname-password-denied-no-will.py'),
    (1, './01-connect-uname-password-denied.py'),
    (1, './01-connect-unix-socket.py'),
    (1, './01-connect-windows-line-endings.py'),
    (2, './01-connect-zero-length-id.py'),

    (1, './02-shared-nolocal.py'),
    (1, './02-shared-qos0-v5.py'),
    (1, './02-subhier-crash.py'),
    (1, './02-subpub-b2c-topic-alias.py'),
    (1, './02-subpub-qos0-long-topic.py'),
    (1, './02-subpub-qos0-oversize-payload.py'),
    (1, './02-subpub-qos0-queued-bytes.py'),
    (1, './02-subpub-qos0-retain-as-publish.py'),
    (1, './02-subpub-qos0-send-retain.py'),
    (1, './02-subpub-qos0-subscription-id.py'),
    (1, './02-subpub-qos0-topic-alias-unknown.py'),
    (1, './02-subpub-qos0-topic-alias.py'),
    (1, './02-subpub-qos1-message-expiry-retain.py'),
    (1, './02-subpub-qos1-message-expiry-will.py'),
    (1, './02-subpub-qos1-message-expiry.py'),
    (1, './02-subpub-qos1-nolocal.py'),
    (1, './02-subpub-qos1-oversize-payload.py'),
    (1, './02-subpub-qos1.py'),
    (1, './02-subpub-qos2-1322.py'),
    (1, './02-subpub-qos2-max-inflight-bytes.py'),
    (1, './02-subpub-qos2-pubrec-error.py'),
    (1, './02-subpub-qos2-receive-maximum-1.py'),
    (1, './02-subpub-qos2-receive-maximum-2.py'),
    (1, './02-subpub-qos2.py'),
    (1, './02-subpub-recover-subscriptions.py'),
    (1, './02-subscribe-dollar-v5.py'),
    (1, './02-subscribe-invalid-utf8.py'),
    (1, './02-subscribe-long-topic.py'),
    (1, './02-subscribe-persistence-flipflop.py'),

    #(1, './03-publish-qos1-queued-bytes.py'),
    (1, './03-pattern-matching.py'),
    (1, './03-publish-bad-flags.py'),
    (1, './03-publish-b2c-disconnect-qos1.py'),
    (1, './03-publish-b2c-disconnect-qos2.py'),
    (1, './03-publish-b2c-qos1-len.py'),
    (1, './03-publish-b2c-qos2-len.py'),
    (1, './03-publish-c2b-disconnect-qos2.py'),
    (1, './03-publish-c2b-qos2-len.py'),
    (1, './03-publish-dollar-v5.py'),
    (1, './03-publish-dollar.py'),
    (1, './03-publish-invalid-utf8.py'),
    (1, './03-publish-long-topic.py'),
    (1, './03-publish-qos1-max-inflight-expire.py'),
    (1, './03-publish-qos1-max-inflight.py'),
    (1, './03-publish-qos1-no-subscribers-v5.py'),
    (1, './03-publish-qos1-retain-disabled.py'),
    (1, './03-publish-qos1.py'),
    (1, './03-publish-qos2-max-inflight-exceeded.py'),
    (1, './03-publish-qos2-max-inflight.py'),
    (1, './03-publish-qos2-reuse-mid.py'),
    (1, './03-publish-qos2.py'),

    (1, './04-retain-check-source-persist.py'),
    (1, './04-retain-check-source.py'),
    (1, './04-retain-clear-multiple.py'),
    (1, './04-retain-qos0-clear.py'),
    (1, './04-retain-qos0-fresh.py'),
    (1, './04-retain-qos0-repeated.py'),
    (1, './04-retain-qos0.py'),
    (1, './04-retain-qos1-qos0.py'),
    (1, './04-retain-upgrade-outgoing-qos.py'),
    (2, './04-retain-check-source-persist-diff-port.py'),

    (1, './05-clean-session-qos1.py'),
    (1, './05-session-expiry-v5.py'),

    (2, './06-bridge-b2br-disconnect-qos1.py'),
    (2, './06-bridge-b2br-disconnect-qos2.py'),
    (2, './06-bridge-b2br-late-connection-retain.py'),
    (2, './06-bridge-b2br-late-connection.py'),
    (2, './06-bridge-b2br-remapping.py'),
    (2, './06-bridge-br2b-disconnect-qos1.py'),
    (2, './06-bridge-br2b-disconnect-qos2.py'),
    (2, './06-bridge-br2b-remapping.py'),
    (2, './06-bridge-clean-session-csF-lcsF.py'),
    (2, './06-bridge-clean-session-csF-lcsN.py'),
    (2, './06-bridge-clean-session-csF-lcsT.py'),
    (2, './06-bridge-clean-session-csT-lcsF.py'),
    (2, './06-bridge-clean-session-csT-lcsN.py'),
    (2, './06-bridge-clean-session-csT-lcsT.py'),
    (2, './06-bridge-fail-persist-resend-qos1.py'),
    (2, './06-bridge-fail-persist-resend-qos2.py'),
    (1, './06-bridge-no-local.py'),
    (2, './06-bridge-outgoing-retain.py'),
    (2, './06-bridge-per-listener-settings.py'),
    (2, './06-bridge-reconnect-local-out.py'),
    (2, './06-bridge-config-reload.py'),

    (1, './07-will-delay-invalid-573191.py'),
    (1, './07-will-delay-reconnect.py'),
    (1, './07-will-delay-recover.py'),
    (1, './07-will-delay-session-expiry.py'),
    (1, './07-will-delay-session-expiry2.py'),
    (1, './07-will-delay.py'),
    (1, './07-will-disconnect-with-will.py'),
    (1, './07-will-invalid-utf8.py'),
    (1, './07-will-no-flag.py'),
    (1, './07-will-null-topic.py'),
    (1, './07-will-null.py'),
    (1, './07-will-oversize-payload.py'),
    (1, './07-will-per-listener.py'),
    (1, './07-will-properties.py'),
    (1, './07-will-qos0.py'),
    (1, './07-will-reconnect-1273.py'),
    (1, './07-will-takeover.py'),

    (2, './08-ssl-bridge.py'),
    (2, './08-ssl-connect-cert-auth-crl.py'),
    (2, './08-ssl-connect-cert-auth-expired.py'),
    (2, './08-ssl-connect-cert-auth-expired-allowed.py'),
    (2, './08-ssl-connect-cert-auth-revoked.py'),
    (2, './08-ssl-connect-cert-auth-without.py'),
    (2, './08-ssl-connect-cert-auth.py'),
    (2, './08-ssl-connect-identity.py'),
    (2, './08-ssl-connect-no-auth-wrong-ca.py'),
    (2, './08-ssl-connect-no-auth.py'),
    (2, './08-ssl-connect-no-identity.py'),
    (1, './08-ssl-hup-disconnect.py'),
    (2, './08-tls-psk-pub.py'),
    (3, './08-tls-psk-bridge.py'),

    (1, './09-acl-access-variants.py'),
    (1, './09-acl-change.py'),
    (1, './09-acl-empty-file.py'),
    (1, './09-auth-bad-method.py'),
    (1, './09-extended-auth-change-username.py'),
    (1, './09-extended-auth-multistep-reauth.py'),
    (1, './09-extended-auth-multistep.py'),
    (1, './09-extended-auth-reauth.py'),
    (1, './09-extended-auth-single.py'),
    (1, './09-plugin-acl-change.py'),
    (1, './09-plugin-auth-acl-pub.py'),
    (1, './09-plugin-auth-acl-sub-denied.py'),
    (1, './09-plugin-auth-acl-sub.py'),
    (1, './09-plugin-auth-context-params.py'),
    (1, './09-plugin-auth-defer-unpwd-fail.py'),
    (1, './09-plugin-auth-defer-unpwd-success.py'),
    (1, './09-plugin-auth-msg-params.py'),
    (1, './09-plugin-auth-unpwd-fail.py'),
    (1, './09-plugin-auth-unpwd-success.py'),
    (1, './09-plugin-auth-v2-unpwd-fail.py'),
    (1, './09-plugin-auth-v2-unpwd-success.py'),
    (1, './09-plugin-auth-v3-unpwd-fail.py'),
    (1, './09-plugin-auth-v3-unpwd-success.py'),
    (1, './09-plugin-auth-v4-unpwd-fail.py'),
    (1, './09-plugin-auth-v4-unpwd-success.py'),
    (1, './09-plugin-auth-v5-unpwd-fail.py'),
    (1, './09-plugin-auth-v5-unpwd-success.py'),
    (1, './09-plugin-bad.py'),
    (1, './09-plugin-change-id.py'),
    (1, './09-plugin-evt-psk-key.py'),
    (1, './09-plugin-delayed-auth.py'),
    (3, './09-plugin-load.py'),
    (1, './09-plugin-publish.py'),
    (1, './09-plugin-tick.py'),
    (1, './09-plugin-unsupported.py'),
    (1, './09-pwfile-parse-invalid.py'),

    (2, './10-listener-mount-point.py'),

    (1, './11-message-expiry.py'),
	(1, './11-persistence-autosave-changes.py'),
    (1, './11-persistent-subscription.py'),
    (1, './11-persistent-subscription-v5.py'),
    (1, './11-persistent-subscription-no-local.py'),
    (1, './11-pub-props.py'),
    (1, './11-subscription-id.py'),

    (1, './12-prop-assigned-client-identifier.py'),
    (1, './12-prop-maximum-packet-size-broker.py'),
    (1, './12-prop-maximum-packet-size-publish-qos1.py'),
    (1, './12-prop-maximum-packet-size-publish-qos2.py'),
    (1, './12-prop-response-topic-correlation-data.py'),
    (1, './12-prop-response-topic.py'),
    (1, './12-prop-server-keepalive.py'),
    (1, './12-prop-subpub-content-type.py'),
    (1, './12-prop-subpub-payload-format.py'),

    (1, './14-dynsec-acl.py'),
    (1, './14-dynsec-allow-wildcard.py'),
    (1, './14-dynsec-anon-group.py'),
    (1, './14-dynsec-auth.py'),
    (1, './14-dynsec-client-invalid.py'),
    (1, './14-dynsec-client.py'),
    (1, './14-dynsec-config-init-env.py'),
    (1, './14-dynsec-config-init-file.py'),
    (1, './14-dynsec-config-init-random.py'),
    (1, './14-dynsec-default-access.py'),
    (1, './14-dynsec-disable-client.py'),
    (1, './14-dynsec-group-invalid.py'),
    (1, './14-dynsec-group.py'),
    (1, './14-dynsec-modify-client.py'),
    (1, './14-dynsec-modify-group.py'),
    (1, './14-dynsec-modify-role.py'),
    (1, './14-dynsec-plugin-invalid.py'),
    (1, './14-dynsec-role-invalid.py'),
    (1, './14-dynsec-role.py'),

	(1, './15-persist-client-msg-in-v3-1-1.py', 'persist_sqlite'),
	(1, './15-persist-client-msg-in-v5-0.py', 'persist_sqlite'),
	(1, './15-persist-client-msg-out-clear-v3-1-1.py', 'persist_sqlite'),
	(1, './15-persist-client-msg-out-dup-v3-1-1.py', 'persist_sqlite'),
	(1, './15-persist-client-msg-out-queue-v3-1-1.py', 'persist_sqlite'),
	(1, './15-persist-client-msg-out-v3-1-1-db.py', 'persist_sqlite'),
	(1, './15-persist-client-msg-out-v3-1-1.py', 'persist_sqlite'),
	(1, './15-persist-client-msg-out-v5-0.py', 'persist_sqlite'),
	(1, './15-persist-client-v3-1-1.py', 'persist_sqlite'),
	(1, './15-persist-client-v5-0.py', 'persist_sqlite'),
	(1, './15-persist-publish-properties-v5-0.py', 'persist_sqlite'),
	(1, './15-persist-retain-clear.py', 'persist_sqlite'),
	(1, './15-persist-retain-v3-1-1.py', 'persist_sqlite'),
	(1, './15-persist-retain-v5-0.py', 'persist_sqlite'),
	(1, './15-persist-subscription-v3-1-1.py', 'persist_sqlite'),
	(1, './15-persist-subscription-v5-0.py', 'persist_sqlite'),

    (1, './16-cmd-args.py'),
    (4, './16-config-huge.py'),
    (1, './16-config-includedir.py'),
    (1, './16-config-parse-errors-tls.py'),
    (1, './16-config-parse-errors-tls-psk.py'),
    (1, './16-config-parse-errors-without-tls.py'),

    (4, './17-control-list-listeners.py'),
    (1, './17-control-list-plugins.py'),
]

ptest.run_tests(tests)
