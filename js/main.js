/*
const hasHighOpenrate = true;
const isRecent = true;
const hasStrongReplyRate = false;
const canBeRecent = true;
const isFlaggedAsSpam = false;

const isHighEngagement =
  hasHighOpenrate &&
  isRecent &&
  (hasStrongReplyRate || canBeRecent) &&
  !isFlaggedAsSpam;
console.log(`The campaign is high-engagement: ${isHighEngagement} `);
*/
/* logical operators 
 && -and;
 || -or;
 ! -Not;
 */

/*switch statement
function billingCost(plan) {
  switch (plan) {
    case "basic":
      return 10.0;
    case "pro":
      return 20.0;
    case "enterprise":
      return 50.0;
    default:
      return 0.0;
  }
}
console.log(
  `The cost for a basic plan is  $${billingCost("basic").toFixed(2)}`,
);
console.log(`The cost for a pro plan is $${billingCost("pro").toFixed(2)} `);
console.log(
  `The cost for a enterprise plan is $${billingCost("enterprise").toFixed(2)}`,
);
console.log(
  `The cost for a  unknown plan is $${billingCost("unknown").toFixed(2)}`,
);
*/
//ternary operator
let isMember = true;
const price = isMember ? "$2.00" : "$10.00";
