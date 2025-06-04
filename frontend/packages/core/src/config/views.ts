import type { ConfigType } from '@plone/registry';
import FileView from '@portalbrasil/core/components/Views/FileView';

export default function install(config: ConfigType) {
  config.views.contentTypesViews = {
    ...config.views.contentTypesViews,
    File: FileView,
  };
  return config;
}
