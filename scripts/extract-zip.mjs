import { execSync } from 'child_process';
import { readdirSync } from 'fs';
import path from 'path';

const zipFile = '/vercel/share/v0-project/b_JDrUkv8a0eC-1772631931078.zip';
const extractDir = '/vercel/share/v0-project/extracted';

// Extract ZIP
execSync(`unzip -o "${zipFile}" -d "${extractDir}"`, { stdio: 'inherit' });

// List extracted contents
console.log('\n--- Extracted contents ---');
function listDir(dir, indent = '') {
  const items = readdirSync(dir, { withFileTypes: true });
  for (const item of items) {
    console.log(`${indent}${item.isDirectory() ? '[DIR]' : ''} ${item.name}`);
    if (item.isDirectory()) {
      listDir(path.join(dir, item.name), indent + '  ');
    }
  }
}
listDir(extractDir);
