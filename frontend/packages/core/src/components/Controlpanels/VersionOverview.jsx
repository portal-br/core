/**
 * Version Overview component.
 * @module components/manage/Controlpanels/VersionOverview
 */
import React from 'react';
import { FormattedMessage } from 'react-intl';
import isEmpty from 'lodash/isEmpty';

import voltoPackageJson from '../../../../../core/packages/volto/package.json';
import projectPackageJson from '../../../../../package.json';

import { defineMessages, useIntl } from 'react-intl';
import config from '@plone/volto/registry';

const messages = defineMessages({
  addons: {
    id: 'Add-ons',
    defaultMessage: 'Add-ons',
  },
  no_addons: {
    id: 'No addons found',
    defaultMessage: 'No addons found',
  },
});

const voltoVersion = voltoPackageJson.version;

const DistributionInfo = (systemInformation) => {
  const { distribution } = systemInformation;
  const { name, title, package_name, package_version } = distribution;
  return (
    <section className="version-group">
      <h3>
        {title} ({name})
      </h3>
      <ul
        style={{
          fontSize: '16px',
          fontFamily: 'Monospace',
          paddingLeft: '1rem',
        }}
      >
        <li>
          {package_name} ({package_version})
        </li>
      </ul>
    </section>
  );
};

const BackendInfo = (systemInformation) => {
  const {
    cmf_version,
    debug_mode,
    pil_version,
    plone_version,
    pb_version,
    pb_gs_metadata_version_installed,
    plone_restapi_version,
    plone_volto_version,
    python_version,
    zope_version,
  } = systemInformation;
  return (
    <section className="version-group">
      <h3>Backend</h3>
      <ul
        style={{
          fontSize: '16px',
          fontFamily: 'Monospace',
          paddingLeft: '1rem',
        }}
      >
        <li>
          PortalBrasil {pb_version} ({pb_gs_metadata_version_installed})
        </li>
        <li>Plone {plone_version}</li>
        <li>plone.volto {plone_volto_version}</li>
        <li>plone.restapi {plone_restapi_version}</li>
        <li>CMF {cmf_version}</li>
        <li>Zope {zope_version}</li>
        <li>Python {python_version}</li>
        <li>PIL {pil_version}</li>
      </ul>
      {debug_mode !== 'No' && (
        <p>
          <FormattedMessage
            id="Warning Regarding debug mode"
            defaultMessage="You are running in 'debug mode'. This mode is intended for sites that are under development. This allows many configuration changes to be immediately visible, but will make your site run more slowly. To turn off debug mode, stop the server, set 'debug-mode=off' in your buildout.cfg, re-run bin/buildout and then restart the server process."
          />
        </p>
      )}
    </section>
  );
};

const FrontendInfo = () => {
  const intl = useIntl();
  const { addonsInfo } = config.settings;
  const isProject = voltoPackageJson.name !== projectPackageJson.name;
  return (
    <section className="version-group">
      <h3>Frontend</h3>
      <ul
        style={{
          fontSize: '16px',
          fontFamily: 'Monospace',
          paddingLeft: '1rem',
        }}
      >
        {isProject ? (
          <li>
            {projectPackageJson.name} {projectPackageJson.version}
          </li>
        ) : null}
        {voltoVersion && <li>Volto {voltoVersion}</li>}
      </ul>
      <h4>{intl.formatMessage(messages.addons)}</h4>
      {isEmpty(addonsInfo) ? (
        <p>{intl.formatMessage(messages.no_addons)}</p>
      ) : (
        <ul style={{ fontSize: '16px', fontFamily: 'Monospace' }}>
          {addonsInfo.map((addon) => (
            <li key={addon.name}>{`${addon.name} ${addon.version || ''}`}</li>
          ))}
        </ul>
      )}
    </section>
  );
};

const VersionOverview = (systemInformation) => {
  return (
    <>
      <DistributionInfo {...systemInformation} />
      <BackendInfo {...systemInformation} />
      <FrontendInfo {...systemInformation} />
    </>
  );
};

export default VersionOverview;
