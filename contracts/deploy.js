async function main() {
  const [deployer] = await ethers.getSigners();
  
  console.log("Deploying contracts with account:", deployer.address);
  console.log("Account balance:", (await deployer.getBalance()).toString());

  const CodeAttestationContract = await ethers.getContractFactory("CodeAttestationContract");
  const contract = await CodeAttestationContract.deploy();

  console.log("CodeAttestationContract deployed to:", contract.address);
  
  // Authorize deployer as attester
  await contract.authorizeAttester(deployer.address);
  console.log("Deployer authorized as attester");
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
