## alb-ingress.tf
resource "helm_release" "alb_ingress" {
  name = "aws-load-balancer-controller"
  repository = "https://aws.github.io/eks-charts"
  chart = "aws-load-balancer-controller"
  namespace = "kube-system"
   set {
    name  = "clusterName"
    value = aws_eks_cluster.eks_cluster.name
  }
}